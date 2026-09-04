// React Theme — extracted from https://solva-template.framer.website/
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
    neutral300: string;
 *   };
 *   fonts: {
    body: string;
 *   };
 *   fontSizes: {
    '12': string;
    '14': string;
    '15': string;
    '16': string;
    '18': string;
    '20': string;
    '28': string;
    '30': string;
    '40': string;
    '48': string;
    '56': string;
 *   };
 *   space: {
    '1': string;
    '16': string;
    '20': string;
    '28': string;
    '32': string;
    '40': string;
    '48': string;
    '60': string;
    '64': string;
    '72': string;
    '96': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    xs: string;
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
    "primary": "#1c1a15",
    "secondary": "#fbfaf6",
    "accent": "#0055ff",
    "background": "#fbfaf6",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#56524a",
    "neutral200": "#ece9e0",
    "neutral300": "#8c887e"
  },
  "fonts": {
    "body": "'Times New Roman', sans-serif"
  },
  "fontSizes": {
    "12": "12px",
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "28": "28px",
    "30": "30px",
    "40": "40px",
    "48": "48px",
    "56": "56px"
  },
  "space": {
    "1": "1px",
    "16": "16px",
    "20": "20px",
    "28": "28px",
    "32": "32px",
    "40": "40px",
    "48": "48px",
    "60": "60px",
    "64": "64px",
    "72": "72px",
    "96": "96px"
  },
  "radii": {
    "sm": "3px",
    "md": "10px",
    "lg": "16px",
    "full": "50px"
  },
  "shadows": {
    "sm": "rgba(0, 85, 255, 0.1) 0px 1px 3px 0px, rgba(0, 85, 255, 0.14) 0px 4px 16px 0px",
    "xs": "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px"
  },
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
      "main": "#1c1a15",
      "light": "hsl(43, 14%, 25%)",
      "dark": "hsl(43, 14%, 10%)"
    },
    "secondary": {
      "main": "#fbfaf6",
      "light": "hsl(48, 38%, 95%)",
      "dark": "hsl(48, 38%, 82%)"
    },
    "background": {
      "default": "#fbfaf6",
      "paper": "#f4f2ec"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0000ee"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "40px",
      "fontWeight": "300",
      "lineHeight": "46px"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "500",
      "lineHeight": "36.4px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "500",
      "lineHeight": "26px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": [
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px",
    "rgba(0, 0, 0, 0.03) 0px 1px 3px 0px, rgba(0, 0, 0, 0.04) 0px 4px 16px 0px, rgba(255, 255, 255, 0.5) 0px 0px 0px 8px",
    "rgba(0, 85, 255, 0.1) 0px 1px 3px 0px, rgba(0, 85, 255, 0.14) 0px 4px 16px 0px"
  ]
};

export default theme;
