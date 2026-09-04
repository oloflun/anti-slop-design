// React Theme — extracted from https://diamondrosesanctuary.com
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '32': string;
    '75.52': string;
    '74.24': string;
    '61.44': string;
    '58.88': string;
    '51.2': string;
    '40.96': string;
    '40.32': string;
    '39.68': string;
    '35.84': string;
    '26.88': string;
    '19.2': string;
 *   };
 *   space: {
    '1': string;
    '24': string;
    '42': string;
    '50': string;
    '73': string;
    '77': string;
    '86': string;
    '120': string;
    '141': string;
    '152': string;
    '182': string;
    '192': string;
    '217': string;
    '254': string;
    '280': string;
    '313': string;
 *   };
 *   radii: {
    xs: string;
    full: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#dfd7c9",
    "secondary": "#20462b",
    "accent": "#1a3822",
    "background": "#dfd7c9",
    "foreground": "#000000",
    "neutral50": "#303030",
    "neutral100": "#000000"
  },
  "fonts": {
    "body": "'NM', sans-serif"
  },
  "fontSizes": {
    "32": "32px",
    "75.52": "75.52px",
    "74.24": "74.24px",
    "61.44": "61.44px",
    "58.88": "58.88px",
    "51.2": "51.2px",
    "40.96": "40.96px",
    "40.32": "40.32px",
    "39.68": "39.68px",
    "35.84": "35.84px",
    "26.88": "26.88px",
    "19.2": "19.2px"
  },
  "space": {
    "1": "1px",
    "24": "24px",
    "42": "42px",
    "50": "50px",
    "73": "73px",
    "77": "77px",
    "86": "86px",
    "120": "120px",
    "141": "141px",
    "152": "152px",
    "182": "182px",
    "192": "192px",
    "217": "217px",
    "254": "254px",
    "280": "280px",
    "313": "313px"
  },
  "radii": {
    "xs": "2px",
    "full": "100px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#dfd7c9",
      "light": "hsl(38, 26%, 95%)",
      "dark": "hsl(38, 26%, 68%)"
    },
    "secondary": {
      "main": "#20462b",
      "light": "hsl(137, 37%, 35%)",
      "dark": "hsl(137, 37%, 10%)"
    },
    "background": {
      "default": "#dfd7c9",
      "paper": "#f2eada"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#303030"
    }
  },
  "typography": {
    "fontFamily": "'NM', sans-serif",
    "h1": {
      "fontSize": "40.96px",
      "fontWeight": "300",
      "lineHeight": "36.864px"
    }
  },
  "shape": {
    "borderRadius": 2
  },
  "shadows": []
};

export default theme;
