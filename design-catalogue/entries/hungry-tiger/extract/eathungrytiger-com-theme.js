// React Theme — extracted from https://www.eathungrytiger.com/
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
    neutral200: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '64': string;
    '128': string;
    '189.44': string;
    '173.44': string;
    '115.2': string;
    '89.6': string;
    '60.16': string;
    '57.6': string;
    '40.32': string;
    '38.4': string;
    '37.12': string;
    '35.84': string;
 *   };
 *   space: {
    '1': string;
    '23': string;
    '28': string;
    '42': string;
    '51': string;
    '61': string;
    '100': string;
    '112': string;
    '122': string;
    '128': string;
    '154': string;
    '172': string;
    '178': string;
    '192': string;
    '245': string;
    '256': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
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
    "primary": "#faae33",
    "secondary": "#402011",
    "accent": "#ffdede",
    "background": "#823513",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#dddddd"
  },
  "fonts": {
    "body": "'Graphikx', sans-serif"
  },
  "fontSizes": {
    "64": "64px",
    "128": "128px",
    "189.44": "189.44px",
    "173.44": "173.44px",
    "115.2": "115.2px",
    "89.6": "89.6px",
    "60.16": "60.16px",
    "57.6": "57.6px",
    "40.32": "40.32px",
    "38.4": "38.4px",
    "37.12": "37.12px",
    "35.84": "35.84px"
  },
  "space": {
    "1": "1px",
    "23": "23px",
    "28": "28px",
    "42": "42px",
    "51": "51px",
    "61": "61px",
    "100": "100px",
    "112": "112px",
    "122": "122px",
    "128": "128px",
    "154": "154px",
    "172": "172px",
    "178": "178px",
    "192": "192px",
    "245": "245px",
    "256": "256px"
  },
  "radii": {
    "sm": "5px",
    "md": "8px",
    "lg": "12px",
    "full": "1280px"
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
      "main": "#faae33",
      "light": "hsl(37, 95%, 74%)",
      "dark": "hsl(37, 95%, 44%)"
    },
    "secondary": {
      "main": "#402011",
      "light": "hsl(19, 58%, 31%)",
      "dark": "hsl(19, 58%, 10%)"
    },
    "background": {
      "default": "#823513",
      "paper": "#281006"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#faae33"
    }
  },
  "typography": {
    "fontFamily": "'Graphikx', sans-serif",
    "h1": {
      "fontSize": "64px",
      "fontWeight": "700",
      "lineHeight": "57.6px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": []
};

export default theme;
